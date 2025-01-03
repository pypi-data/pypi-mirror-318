from time import sleep

from pysnurr import SPINNERS, Snurr


def demo_basic() -> None:
    """Demo basic spinner usage"""
    print("\n=== Basic Usage ===")

    print("\nContext manager (recommended):")
    with Snurr():
        sleep(2)  # Simulate work

    print("\nTraditional usage:")
    spinner = Snurr()
    spinner.start()
    sleep(2)  # Simulate work
    spinner.stop()


def demo_styles() -> None:
    """Demo all available spinner styles"""
    print("\n=== Spinner Styles ===")

    for name, style in SPINNERS.items():
        style_name = f"{name} (default)" if name == "CLASSIC" else name
        print(f"\nStyle: {style_name}")
        with Snurr(symbols=style):
            sleep(2)


def demo_with_output() -> None:
    """Demo spinner with concurrent stdout writes"""
    print("\n=== Spinner with Output ===")

    # Using synchronized write method
    print("\nUsing synchronized write method:")
    with Snurr(symbols=SPINNERS["EARTH"]) as spinner:
        spinner.write("Starting a long process...")
        sleep(1)
        spinner.write("Step 1: Data processing")
        sleep(1)
        spinner.write("Step 2: Analysis complete")
        sleep(1)

    # Spinner at end of line with synchronized writes
    print("\nSpinner at end of line:")
    with Snurr(symbols=SPINNERS["HEARTS"]) as spinner:
        for i in range(3):
            spinner.write(f"\rLine {i+1} while spinning", end=" ")
            sleep(1)

    print("\nDone!")


def demo_custom() -> None:
    """Demo custom spinner configuration"""
    print("\n=== Custom Spinner ===")
    print("Custom symbols and slower speed:")
    with Snurr(symbols="◉◎", delay=0.5):
        sleep(4)


if __name__ == "__main__":
    print("=== Snurr Spinner Demo ===")
    print("Press Ctrl+C to exit at any time")

    try:
        demo_basic()
        demo_styles()
        demo_with_output()
        demo_custom()

        print("\nDemo completed! 🎉")
    except KeyboardInterrupt:
        print("\nDemo interrupted by user")
