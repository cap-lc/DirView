from pathlib import Path
import sys
import os

TAB  = "   "
JUMP = "│  "
NEXT = "├──"
LAST = "└──"

def directory_view(dir: Path, tab: str = "", 
                   head_name: bool = True,
                   minimalist: bool = False) -> list[str] :
    output: list[str] = []
    if head_name: output.append(dir.name)

    ext_set: set[str] = set()
    
    info: list[tuple[Path, str, bool]] = []
    if minimalist :
        ext: set[str] = set()
        for elem in dir.iterdir() :
            ext_ = elem.suffix
            if ext_ in ext: continue
            ext.add(ext_)
            
            name = f"file(s){elem.suffix}"
            if elem.is_dir(): name = elem.name
            
            info.append((elem, name, elem.is_dir()))
    else :
        info = [
            (elem, elem.name, elem.is_dir()) for elem in dir.iterdir()
        ]
    
    i_max = len(info)-1
    for i, (path, name, is_dir) in enumerate(info) :
        is_last = i == i_max

        tab_elem = NEXT
        if is_last : tab_elem = LAST

        output.append(f"{tab}{tab_elem}{name}")

        if is_dir :
            new_tab = JUMP
            if is_last : new_tab = TAB
            extend = directory_view(path, tab + new_tab, False, minimalist)
            output.extend(extend)

    return output

def main():
    argv = sys.argv[1:]

    dir = Path(os.getcwd())
    m = False
    fail = False

    dir_p: bool = False
    m_p: bool = False
    c: int = 0

    while(len(argv) > 0):
        c += 1
        arg = argv.pop()

        if c > 2 :
            print("Too many arguments")
            fail = True
            break

        if arg == "-m":
            if m_p :
                print("'-m' can only be parsed once")
                fail = True
                break
            m = True

        else :
            
            if dir_p :
                print("Only one folder can be processed")
                fail = True
                break

            if arg == "cwd":
                # print("arg == 'cwd'")
                dir = Path(os.getcwd())

            elif arg.startswith("."):
                # print("arg.startswith('.')")
                dir = Path(f"{os.getcwd()}/{arg[1:]}")

            else : 
                # print("else")
                dir = Path(arg)

            if not dir.exists():
                print(f"Unable to find Path from : {dir}")
                fail = True
                break
            
            if not dir.is_dir(): dir = dir.parent

    if not fail :
        print("\n".join(directory_view(dir, minimalist=m)))

if __name__ == "__main__" :
    print(sys.argv)