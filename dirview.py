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
    
    iter = list(dir.iterdir())
    i_max = len(iter)-1
    for i, elem in enumerate(iter) :
        ext = elem.suffix
        is_last = i == i_max
        is_dir = elem.is_dir()
        is_old = ext in ext_set

        if minimalist and is_old: continue

        tab_elem = NEXT
        if is_last : tab_elem = LAST

        to_display: str = elem.name
        if minimalist and not is_dir: 
            to_display = f"file(s){ext}"
            ext_set.add(ext)
        output.append(f"{tab}{tab_elem}{to_display}")

        if is_dir :
            new_tab = JUMP
            if is_last : new_tab = TAB
            extend = directory_view(elem, tab + new_tab, False, minimalist)
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
                dir = Path(os.getcwd())

            elif arg.startswith("./"):
                dir = Path(f"{os.getcwd()}/{arg[1:]}")

            else : dir = Path(arg)

            if not dir.exists():
                print(f"Unable to find Path from : {dir}")
                fail = True
                break

    if not fail :
        print("\n".join(directory_view(dir, minimalist=m)))

if __name__ == "__main__" :
    print(sys.argv)