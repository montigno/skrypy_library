class ChooseRepertories:
    def __init__(self):
        from subprocess import Popen, PIPE
        import os
        import sys
        dir_path = os.path.dirname(os.path.realpath(__file__))
        programm = os.path.join(dir_path, 'sources')
        command = 'java -cp ' + programm + " FileChooser"
        p = Popen(command, stdin=PIPE, stdout=PIPE, stderr=PIPE, shell=True)
        txt, error = p.communicate()
        rc = p.returncode
        txt = txt.decode("utf-8")
        self.outRep = []
        self.outFiles = []
        for val in txt.split("\n"):
            if 'rep=' in val:
                self.outRep.append(val[4:])
            elif 'file=' in val:
                self.outFiles.append(val[5:])

    def list_repertories(self: 'list_path'):
        return self.outRep

    def list_files(self: 'list_path'):
        return self.outFiles
