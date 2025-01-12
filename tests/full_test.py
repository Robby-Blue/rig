import pytest

import sys
import os

tests_folder = os.path.dirname(__file__)
sys.path.insert(0, os.path.join(tests_folder, "../src"))

import language as language
import intermediates
from component import Component

def get_by_type(search_type, arr):
    return [e for e in arr if isinstance(e, search_type)]

def src_to_elements(src):
    ir = language.compile(src, "testing")
    root_component = Component.read_child_component(ir["fig"], {}, src)
    intermediate = root_component.to_intermediate()
    return intermediate["children"]

def test_relative_start():
    elements = src_to_elements("""
def fig() {
    svg(100, 100) {
        rect(x: 0, y: 0, width: 50)
    }
}
""")

    rect = get_by_type(intermediates.IntermediateRect, elements)[0]

    assert rect.get("x") == pytest.approx(0, abs=1)

def test_relative_end():
    elements = src_to_elements("""
def fig() {
    svg(100, 100) {
        rect(x: 100, y: 0, width: 50)
    }
}
""")

    rect = get_by_type(intermediates.IntermediateRect, elements)[0]

    assert rect.get("x") == pytest.approx(50, abs=1)

def test_relative_middle():
    elements = src_to_elements("""
def fig() {
    svg(100, 100) {
        circle(x: 50, y: 50, size: 10)
    }
}
""")

    circle = get_by_type(intermediates.IntermediateCircle, elements)[0]

    assert circle.get("x") == pytest.approx(50, abs=1)

def test_hlist_fill():
    elements = src_to_elements("""
def fig() {
    svg(100, 100, layout: hlist()) {
        rect()
        rect()
    }
}
""")

    rects = get_by_type(intermediates.IntermediateRect, elements)

    assert rects[0].get("x") == pytest.approx(0, abs=1)
    assert rects[1].get("x") == pytest.approx(50, abs=1)

def test_hlist_fill_auto():
    elements = src_to_elements("""
def fig() {
    svg(100, 100, layout: hlist()) {
        rect()
        rect(width: 75)
    }
}
""")

    rects = get_by_type(intermediates.IntermediateRect, elements)

    assert rects[0].get("x") == pytest.approx(0, abs=1)
    assert rects[1].get("x") == pytest.approx(25, abs=1)

def test_hlist_fill_set():
    elements = src_to_elements("""
def fig() {
    svg(100, 100, layout: hlist()) {
        rect(width: 10)
        rect(width: 10)
        rect(width: 10)
    }
}
""")

    rects = get_by_type(intermediates.IntermediateRect, elements)

    assert rects[0].get("x") == pytest.approx(0, abs=1)
    assert rects[1].get("x") == pytest.approx(10, abs=1)
    assert rects[2].get("x") == pytest.approx(20, abs=1)

def test_hlist_between():
    elements = src_to_elements("""
def fig() {
    svg(100, 100, layout: hlist(space: "space_between")) {
        rect(width: 10)
        rect(width: 10)
    }
}
""")

    rects = get_by_type(intermediates.IntermediateRect, elements)

    assert rects[0].get("x") == pytest.approx(0, abs=1)
    assert rects[1].get("x") == pytest.approx(90, abs=1)