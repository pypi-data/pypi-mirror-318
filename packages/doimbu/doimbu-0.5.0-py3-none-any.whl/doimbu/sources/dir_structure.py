from pathlib import Path


def get_variants_list(root_dir: Path) -> list[str]:
    """Generates a list of variants based on subdir names of:
     [PROJECT_ROOT]/variants

    :return: list of variants
    """
    variants_dir = root_dir / 'variants'
    variants = []

    if variants_dir.is_dir():
        for variant in variants_dir.iterdir():
            if variant.is_dir():
                pass

        variants = [variant.name
                    for variant in variants_dir.iterdir() if variant.is_dir()]

    return variants