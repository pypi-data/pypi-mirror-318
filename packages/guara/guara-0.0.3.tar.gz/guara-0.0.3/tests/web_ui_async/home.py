from caqui import synchronous
from guara.transaction import AbstractTransaction


class GetNthLink(AbstractTransaction):
    """
    Get the nth link from the page

    Args:
        link_index (int): The index of the link
        with_session (object): The session of the Web Driver
        connect_to_driver (str): The URL to connect the Web Driver server

    Returns:
        str: The nth link
    """

    def __init__(self, driver):
        super().__init__(driver)

    def do(
        self,
        link_index,
        with_session,
        connect_to_driver,
    ):
        locator_type = "xpath"
        locator_value = f"//a[@id='a{link_index}']"
        anchor = synchronous.find_element(
            connect_to_driver, with_session, locator_type, locator_value
        )
        return synchronous.get_text(connect_to_driver, with_session, anchor)


class GetAllLinks(AbstractTransaction):
    """
    Get the list of links from the page

    Args:
        with_session (object): The session of the Web Driver
        connect_to_driver (str): The URL to connect the Web Driver server

    Returns:
        str: The list of links
    """

    def __init__(self, driver):
        super().__init__(driver)

    def do(self, with_session, connect_to_driver):
        links = []
        MAX_INDEX = 4

        for i in range(MAX_INDEX):
            i += 1
            links.append(
                # Instead of duplicate the code it is possible to call transactions directly
                GetNthLink(None).do(
                    link_index=i,
                    with_session=with_session,
                    connect_to_driver=connect_to_driver,
                )
            )
        # uncomment it to see the instances of the browser for a while
        # import time
        # time.sleep(2)
        return links
