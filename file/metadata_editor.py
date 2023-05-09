import subprocess

class MetadataEditor:
    def add_metadata(self, file, metadata):
        """Adds metadata to a file using exiftool."""
        cmd = ["exiftool"]
        for k, v in metadata.items():
            cmd += [f"-{k}={v}"]
        cmd += [file]
        subprocess.run(cmd)

    def delete_metadata(self, file, metadata_keys=None):
        """Deletes metadata from a file using exiftool."""
        if metadata_keys == None:
            metadata_keys = [
                "GPS Latitude Ref",
                "GPS Longitude Ref",
                "GPS Altitude Ref",
                "GPS Speed Ref",
                "GPS Speed",
                "GPS Img Direction Ref",
                "GPS Img Direction",
                "GPS Dest Bearing Ref",
                "GPS Dest Bearing",
                "GPS Date Stamp",
                "GPS Horizontal Positioning",
                "GPS Altitude",
                "GPS Latitude",
                "GPS Longitude",
                "GPS Position",
                "Lens Id",
                # "Camera Model Name",
                "Host Computer",
                "Software"
            ]

        cmd = ["exiftool"]
        for k in metadata_keys:
            key = k.replace(" ", "")
            cmd += [f"-{key}="]
        cmd += [file]
        print(cmd)
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
    print("GET METADATA")
    print(meta)

    
    print("\n\nDELETE METADATA")
    deleted_meta = metaclass.delete_metadata(file=file)

    meta = metaclass.get_metadata(file=file)
    print("\n\nCHECK METADATA")
    print(meta)
    