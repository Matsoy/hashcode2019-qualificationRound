class Photo:
    def __init__(self, lid, tags_list, orientation):
        """
        Constructor

        :param lid:         Photo identifier
        :param tags_list:   List of tags
        :param orientation: Orientation. "H" for horizontal or "V" for vertical
        """
        self.id          = lid
        self.tags_list     = tags_list
        self.orientation = orientation