from pathlib import Path
import sys
import os

TAB  = "   "
JUMP = "│  "
NEXT = "├──"
LAST = "└──"

def directory_view_print(dir: Path, tab: str = "", 
                   head_name: bool = True,
                   minimalist: bool = False) -> None :
    
    if head_name: print(dir.name)
    
    info: list[tuple[Path, str, bool]] = []
    if minimalist :
        ext: set[str] = set()
        for elem in dir.iterdir() :
            is_dir = elem.is_dir()
            suffix = elem.suffix
                
            if (suffix in ext) and (not is_dir): continue
            ext.add(suffix)
            
            name = f"file(s){suffix}"
            if is_dir: name = elem.name
            
            info.append((elem, name, is_dir))
    else :
        info = [
            (elem, elem.name, elem.is_dir()) for elem in dir.iterdir()
        ]
    
    i_max = len(info)-1
    for i, (path, name, is_dir) in enumerate(info) :
        is_last = i == i_max

        tab_elem = NEXT
        if is_last : tab_elem = LAST

        print(f"{tab}{tab_elem}{name}")

        if is_dir :
            new_tab = JUMP
            if is_last : new_tab = TAB
            directory_view_print(path, tab + new_tab, False, minimalist)

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
        directory_view_print(dir, minimalist=m)

if __name__ == "__main__" :
    print(sys.argv)