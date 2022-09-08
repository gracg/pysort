
class NotSortedException(Exception):

    def __init__(self,original_list,checked_list):
        self.message = "List not sorted \n" \
                       "Original list: {} \n" \
                       "Sorted list: {}".format(original_list,checked_list)

        super().__init__(self.message)
