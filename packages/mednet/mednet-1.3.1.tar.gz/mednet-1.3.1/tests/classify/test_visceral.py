# SPDX-FileCopyrightText: Copyright © 2023 Idiap Research Institute <contact@idiap.ch>
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""Tests for VISCERAL dataset."""

import pytest
from click.testing import CliRunner


def id_function(val):
    if isinstance(val, dict):
        return str(val)
    return repr(val)


@pytest.mark.parametrize(
    "split,lenghts",
    [
        ("default", dict(train=241, validation=69, test=35)),
    ],
    ids=id_function,  # just changes how pytest prints it
)
def test_protocol_consistency(
    database_checkers,
    split: str,
    lenghts: dict[str, int],
):
    from mednet.data.split import make_split

    database_checkers.check_split(
        make_split("mednet.config.classify.data.visceral", f"{split}.json"),
        lengths=lenghts,
        prefixes=("16/10000"),
        possible_labels=(0, 1),
    )


@pytest.mark.skip_if_rc_var_not_set("datadir.visceral")
def test_database_check():
    from mednet.scripts.database import check

    runner = CliRunner()
    result = runner.invoke(check, ["visceral"])
    assert (
        result.exit_code == 0
    ), f"Exit code {result.exit_code} != 0 -- Output:\n{result.output}"
