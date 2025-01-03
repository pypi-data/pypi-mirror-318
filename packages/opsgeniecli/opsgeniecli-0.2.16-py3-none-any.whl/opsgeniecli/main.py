from opsgeniecli.opsgeniecli import bootstrapper


def cli():
    """Main entry point of tool"""
    bootstrapper(
        obj={}
    )  # pylint: disable=no-value-for-parameter, unexpected-keyword-arg


if __name__ == "__main__":
    cli()