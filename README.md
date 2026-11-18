# DirView
il s'agit d'un outil pour voir le contenue de dossier en ajoutant la commande terminal `dirview`

### Utilisation
Par défaut `dirview` détail ce qui se trouve dans le dossier actuellement ouvert par le terminal :
```cmd
PS C:\path\to\folder> dirview
folder
├──dir1
│  ├──dir2
│  │  └──file21.f90
│  ├──file11.txt
│  └──file12.md
├──file1.txt
├──file2.txt
└──file3.zip
```

Un chemin vers un dossier ou fichier peut être donné pour observé le contenue du dit dossier (ou du dossier contenant le fichier)
```cmd
PS C:\path\from\elsewhere> dirview "C:\path\to\folder\file1.txt"
folder
├──dir1
│  ├──dir2
│  │  └──file21.f90
│  ├──file11.txt
│  └──file12.md
├──file1.txt
├──file2.txt
└──file3.zip
```
`cwd` permet aussi de se référer dossier actuellement ouvert


Une option `-m` permet de limiter le nombre de fichiers affichés en se limitant à l'énumération des type de fichier
```cmd
PS C:\path\to\folder> dirview -m
folder
├──file(s)
│  ├──file(s)
│  │  └──file(s).f90
│  ├──file(s).txt
│  └──file(s).md
├──file(s).txt
└──file(s).zip
```

Les options `-m` et de chemin imposé sont compatible peut import leur ordre