Files:
1.  hello
2.  Grid
3.  Button
4.  Entry
5.  Entry Extra
6.  Calculator
7.  Images
8.  ImageViwer (Open Multiple Images, Status at bottom )
9.  Frame
10. Radio
11. Radio2 - Loop
12. MessageBox 
13. New Window
14. Open File Dialog Box
15. Slider
16. CheckBox (int value) & CheckBox2 (String Value)
17. DropDown Menus 
18. Database
19. Web API - Weather report
20. Matplot library

```
## Make file executable:
> pyinstaller --onefile -w 'filename.py'
```

```
## Adding Icon to app:
> pyinstaller.exe --onefile --windowed --icon="Path_of_.ico_file" app.py
```

```

## Create a spec file with all defaults
> pyi-makespec myapp.py
```

```

## Or, if you want the final distributable package to be a single file
> pyi-makespec myapp.py -F
```

```

## To set the icon
> pyi-makespec myapp.py --icon=icon.ico
```
```

## To disable console
> pyi-makespec myapp.py --noconsole
```
```

## Combined
> pyi-makespec myapp.py -F --icon=icon.ico --noconsole
```
```

## Build the .spec file
> pyinstaller myapp.spec
```

```
## Show all the installed packages
> pip freeze
```
