from ..huskypo import logstack, logconfig


logconfig.basic()


def first():
    logstack.info("from first.")


def test():
    first()


test()
