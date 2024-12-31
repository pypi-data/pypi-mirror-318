"""Test module for the class PictorRect."""

from assertpy import assert_that

from src.pictor_lib.pictor_point import PictorPoint
from src.pictor_lib.pictor_rect import PictorRect
from src.pictor_lib.pictor_size import PictorSize


# pylint: disable=too-many-public-methods
class TestPictorRect:
    """Tests for the class PictorRect."""

    def test_properties(self):
        """Test for properties."""

        rect = PictorRect(point=PictorPoint(67, 42), size=PictorSize(7, 5))

        # Verify rect.
        assert_that(rect.top).is_equal_to(42)
        assert_that(rect.bottom).is_equal_to(47)
        assert_that(rect.left).is_equal_to(67)
        assert_that(rect.right).is_equal_to(74)
        assert_that(rect.top_left).is_equal_to(PictorPoint(67, 42))
        assert_that(rect.top_center).is_equal_to(PictorPoint(70.5, 42))
        assert_that(rect.top_right).is_equal_to(PictorPoint(74, 42))
        assert_that(rect.left_center).is_equal_to(PictorPoint(67, 44.5))
        assert_that(rect.center).is_equal_to(PictorPoint(70.5, 44.5))
        assert_that(rect.right_center).is_equal_to(PictorPoint(74, 44.5))
        assert_that(rect.bottom_left).is_equal_to(PictorPoint(67, 47))
        assert_that(rect.bottom_center).is_equal_to(PictorPoint(70.5, 47))
        assert_that(rect.bottom_right).is_equal_to(PictorPoint(74, 47))
        assert_that(rect.size).is_equal_to(PictorSize(7, 5))

    def test_to_string(self):
        """Test for converting to string."""

        rect = PictorRect(point=PictorPoint(67, 42), size=PictorSize(7, 5))

        # Verify rect.
        assert_that(str(rect)).is_equal_to('7.00x5.00+67.00+42.00')
        assert_that(repr(rect)).is_equal_to('7.00x5.00+67.00+42.00')
