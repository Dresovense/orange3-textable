.. meta::
   :description: Orange Textable documentation, table construction widgets
   :keywords: Orange, Textable, documentation, table, construction, widgets

Table construction widgets
==========================

Widgets of this category take *Segmentation* data in input and emit tabular
data in the internal format of Orange Textable. They are thus ultimately
responsible for converting text to tables, either by counting items
(:doc:`Count <widgets/count>`), by measuring their length (:doc:`Length <widgets/length>`), by quantifying
their diversity (:doc:`Variety <widgets/variety>`). Widget :doc:`Cooccurrence <widgets/cooccurrence>` makes
it possible to measure the tendency of text units to occur in the same contexts,
while :doc:`Context <widgets/context>` serves to build concordances and collocation lists.
Finally, :doc:`Category <widgets/category>` exploits categorical information associated with
segmentations.

.. toctree::
    :maxdepth: 1

    Count <widgets/count>
    Length <widgets/length>
    Variety <widgets/variety>
    Cooccurrence <widgets/cooccurrence>
    Context <widgets/context>
    Category <widgets/category>

