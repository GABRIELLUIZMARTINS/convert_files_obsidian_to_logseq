# Convert_files_obsidian_to_logseq

Convert files obsidian to logseq.

## Convertion files

Convert files following structure of files `![[file_name.extension|size]]` or `![[file_name.extension]]` from *Obsidian* to `![file_name]('../assets/file_name.extension')` *Logseq*.

## Generate Executable

To generate the executable you can use the following command:

    $ python -m PyInstaller --onefile --windowed --add-data="src;." --add-data="assets;assets" --name="ObsidianToLogseq" --icon="assets/obs2log.ico" --distpath App --workpath="." src/
    main.py

After executing this command, the exacutable will be availeble in the `App` folder.
