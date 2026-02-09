import settings

class PSOIsoFile(settings.UserFilePath):
    """
    Locate the user's Phantasy Star Online Episode I & II Plus ISO file.
    """

    description = "Phantasy Star Online Episode I & II Plus ISO"
    copy_to = None


class PSOSettings(settings.Group):
    iso_file: PSOIsoFile = PSOIsoFile(PSOIsoFile.copy_to)