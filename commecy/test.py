# commecy -- normalizer for french for spacy.
# Copyright (C) 2024,2025  thjbdvlt
#
# commecy is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 3 of the License,
# or (at your option) any later version.
#
# commecy is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with commecy.  If not, see <https://www.gnu.org/licenses/>.


from .normalizer import _getdata
from .normalizer import CommeCyNormalizer


def test():
    """Tests the normalizer."""

    normalizer = CommeCyNormalizer(nlp=None)
    data = _getdata("test.csv")
    data = [i.strip().split(",") for i in data]
    for form, norm in data:
        result = normalizer.normalize(form)
        if norm != result:
            raise ValueError(
                "Failed normalization of:",
                form,
                "\nWaits:",
                norm,
                "\nGets:",
                result,
            )
