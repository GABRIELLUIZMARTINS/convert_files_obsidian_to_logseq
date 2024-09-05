from obsidian2logseq import *

if __name__ == '__main__':

    pf = Constants()
    # Files path Obsidian
    obsidian_files = pf.get_path()

    #Convert files
    obj_convert = obsidian_to_logseq(obsidian_files)
    obj_convert.convert_files()