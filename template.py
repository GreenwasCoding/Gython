# GYTHON PACKAGES #
import Gython as console
from Gython import GyPlus as GPlus, GyWebPackages
from Gython import ColorPanel as GColors
from Gython import GyWebPackages as GWeb
# CODE HERE #
console.Say(f"{GColors.GREEN}{console.WelcomeMessage}{GColors.RESET}")
console.Say(f"Your Current Version is: {console.Version}")
GPlus.Warn(f"Please read the license in [https://github.com/GreenwasCoding/Gython/blob/main/LICENSE]", level=4)
