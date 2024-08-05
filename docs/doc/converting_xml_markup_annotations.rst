**1. Converting XML markup to annotations**
===========================================

Often, the best way (and sometimes the only way) to add a specific type
of annotation to a text is by “manually” adding it to the data. This is
frequently done with XML markup. For instance, the text that appears in
the :doc:`Text Field <widgets/text_field>` instance of :ref:`figure 1 <converting_xml_markup_annotations_fig1>`
below is segmented into words by means of *<w>* tags whose *type*
attribute indicates the “part of speech” associated with each word (e.g.
*DET*, *NOUN*, *PREP*, and so on).

.. _converting_xml_markup_annotations_fig1:

.. figure:: figures/text_field_xml_example.png
    :align: center
    :alt: Sample text annotated using XML markup

    Figure 1: Sample text annotated using XML markup.

The role of widget :doc:`Extract XML <widgets/extract_xml>`
is to convert XML markup into annotated segments . In its basic version
(see :ref:`figure 2 <converting_xml_markup_annotations_fig2>`
below), the widget’s interface essentially requires the user to specify
the name of the XML tags that must be imported, namely *w* in this
example. The **Remove markup** checkbox indicates whether further markup
(if any) detected *within* imported tags must be removed (there is no
further markup in this example, so that this option has no effect here).

.. _converting_xml_markup_annotations_fig2:

.. figure:: figures/extract_xml_example.png
    :align: center
    :alt: Interface of the Extract XML widget

    Figure 2: Interface of the :doc:`Extract XML <widgets/extract_xml>` widget.

After connecting the above :doc:`Text Field <widgets/text_field>`
and :doc:`Extract XML <widgets/extract_xml>`
instances, and the latter to an instance of
:doc:`Display <widgets/display>`,
you can verify that the resulting segmentation contains a segment for
the content of each *<w>* tag in the input text, and that this segment
is annotated with key *type* and value *DET*, *NOUN*, or *PREP* (the
three first such segments are shown on :ref:`figure 3 <converting_xml_markup_annotations_fig3>`
below). Each attribute-value pair of each XML tag has indeed been
automatically converted to a *{key: value}* annotation.

.. _converting_xml_markup_annotations_fig3:

.. figure:: figures/display_xml_annotations_example.png
    :align: center
    :alt: Annotations imported using Extract XML

Figure 3: Annotations imported using :doc:`Extract XML <widgets/extract_xml>`.

**1.1. See also**
-----------------

- :doc:`Reference: Extract XML widget <widgets/extract_xml>`
- :doc:`Cookbook: Convert XML tags to Orange Textable annotations <convert_xml_tags_annotations>`