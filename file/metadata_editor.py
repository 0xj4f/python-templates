import subprocess

class MetadataEditor:
    def add_metadata(self, file, metadata):
        """Adds metadata to a file using exiftool."""
        cmd = ["exiftool"]
        for k, v in metadata.items():
            cmd += [f"-{k}={v}"]
        cmd += [file]
        subprocess.run(cmd)

    def delete_metadata(self, file, metadata_keys):
        """Deletes metadata from a file using exiftool."""
        cmd = ["exiftool"]
        for k in metadata_keys:
            cmd += [f"-{k}="]
        cmd += [file]
        subprocess.run(cmd)

    def get_metadata(self, file):
        """Gets the metadata of a file using exiftool."""
        cmd = ["exiftool", "-j", file]
        result = subprocess.run(cmd, stdout=subprocess.PIPE)
        return result.stdout.decode()

    def modify_metadata(self, file, metadata):
        """Modifies the metadata of a file using exiftool."""
        cmd = ["exiftool"]
        for k, v in metadata.items():
            cmd += [f"-{k}={v}"]
        cmd += [file]
        subprocess.run(cmd)


if __name__ == '__main__':
    import sys
    file = sys.argv[1]
    metaclass = MetadataEditor()
    meta = metaclass.get_metadata(file=file)
    print(meta)