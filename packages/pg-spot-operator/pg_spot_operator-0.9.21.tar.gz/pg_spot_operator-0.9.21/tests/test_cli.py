# from pg_spot_operator.cli import (
#     ArgumentParser,
#     compile_manifest_from_cmdline_params,
# )
#
#
# def test_compile_manifest():
#     args: ArgumentParser = ArgumentParser()
#     args.instance_name = "x"
#     args.region = "y"
#
#     args.aws_security_group_ids = "x,y"
#     m = compile_manifest_from_cmdline_params(args)
#     assert len(m.aws.security_group_ids) == 2
#
#     args.aws_security_group_ids = ""
#     m = compile_manifest_from_cmdline_params(args)
#     assert len(m.aws.security_group_ids) == 0


## TODO
# tests/test_cli.py:3: in <module>
#     from pg_spot_operator.cli import (
# pg_spot_operator/cli.py:8: in <module>
#     from prettytable import PrettyTable
# E   ModuleNotFoundError: No module named 'prettytable'
