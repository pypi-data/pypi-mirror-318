from huskypo import SwipeAction, SwipeBy


class MySwipe:

    # (B, D, F)

    BA_VA_FA = SwipeAction(SwipeBy.BC, SwipeBy.VC, SwipeBy.FC)
    BA_VA_FR = SwipeAction(SwipeBy.BC, SwipeBy.VC, SwipeBy.FP)

    BA_VA_FA = SwipeAction(SwipeBy.BC, SwipeBy.VC, SwipeBy.FC)
    BA_VA_FR = SwipeAction(SwipeBy.BC, SwipeBy.VC, SwipeBy.FP)


# border: 2
# direction: 2x2=4
# fix: 2
# total = 2x4x2=16
