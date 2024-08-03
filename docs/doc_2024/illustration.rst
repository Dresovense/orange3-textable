textable_doc_removed.rst**Illustration: mining Humanist**
=================================

The following example is meant to show *what* Orange Textable typically
does, without considering (for now) every detail of *how* it does it.

In a paper reflecting on terminology in the field of Digital Humanities
[#]_, Patrik Svensson compares the evolution of the frequency of expressions
*Humanities Computing* and *Digital Humanities* over 20 years of
archives of the `Humanist discussion group <http://dhhumanist.org/>`_.
He uses these figures to show that while the former denomination remains
prevalent over these two decades, the latter has been quickly gaining
ground since the 2000s.

The same experiment can be run with Orange Textable, by building a
“visual program” like the one shown on :ref:`figure 1 <illustration_fig1>` below:


.. _illustration_fig1:

.. figure:: figures/mining_humanist_schema.png
    :align: center
    :alt: Mining Humanist with an Orange Textable schema
    :scale: 80%

    Figure 1: Mining Humanist with an Orange Textable schema.

Figure 1: Mining Humanist with an Orange Textable workflow.

Such a program is called a *workflow*. Its visible part consists of a
network of interconnected units called *widget instances*. Each instance
belongs to a type, e.g.
`URLs <https://orange3-textable.readthedocs.io/en/latest/urls.html#urls>`__,
`Recode <https://orange3-textable.readthedocs.io/en/latest/recode.html#recode>`__,
`Segment <https://orange3-textable.readthedocs.io/en/latest/segment.html#segment>`__,
and so on. Widgets are the basic blocks with which a variety of text
analysis applications can be built. Each corresponds to a fundamental
operation, such as “import data from an online source”
(`URLs <https://orange3-textable.readthedocs.io/en/latest/urls.html#urls>`__)
or “replace specific text patterns with others”
(`Recode <https://orange3-textable.readthedocs.io/en/latest/recode.html#recode>`__)
for example. Connections between instances determine the flow of data in
the workflow, and thus the order in which operations are carried on.
Several parallel paths can be constructed, as demonstrated here by the
`Recode <https://orange3-textable.readthedocs.io/en/latest/recode.html#recode>`__
instance, which sends data to
`Segment <https://orange3-textable.readthedocs.io/en/latest/segment.html#segment>`__
as well as
`Count <https://orange3-textable.readthedocs.io/en/latest/count.html#count>`__.

Widget instances can be individually parameterized in order to
“fine-tune” their operation. For example, double-clicking on the
`Recode <https://orange3-textable.readthedocs.io/en/latest/recode.html#recode>`__
instance of `figure
1 <https://orange3-textable.readthedocs.io/en/latest/illustration.html#illustration-fig1>`_
above displays the interface shown on `figure
2 <https://orange3-textable.readthedocs.io/en/latest/illustration.html#illustration-fig2>`__
below. What this particular configuration means is that every line
beginning with symbol \| or >
(`Regex <https://orange3-textable.readthedocs.io/en/latest/note_regular_expressions.html>`__
field) should be replaced with an empty string (**Replacement string**):
in other words, remove those lines that are marked as being part of a
reply to another message. There is a fair amount of variation between
widget interfaces, but regular expressions play an important role in
several of them and Orange Textable’s flexibility owes a lot to them.

|Interface of Recode widget in the Humanist example|

Figure 2: Interface of the
`Recode <https://orange3-textable.readthedocs.io/en/latest/recode.html#recode>`__
widget.

After executing the workflow of `figure
1 <https://orange3-textable.readthedocs.io/en/latest/illustration.html#illustration-fig1>`__
above, the resulting frequencies can be viewed by double-clicking on the
**Data Table** instance, whose interface is shown on `figure
3 <https://orange3-textable.readthedocs.io/en/latest/illustration.html#illustration-fig3>`__
below. On the whole, these figures lend themselves to the same
interpretation as that of Patrik Svensson, but they differ wildly from
the frequencies he reports. This might be explained by the fact that, in
the present illustration, we have used *preprocessed* data made
available on the Humanist website, or it might be that we have not
processed the data exactly like Svensson did. The user can always refer
to the Orange Textable workflow (including the parameters of each
instance) to understand exactly the operations that it performs.
[#]_ In this sense, Orange Textable does not only attempt to make the
construction of text analysis programs easier; it aims to make
*communicating* and *understanding* such programs easier.

|Monitoring the frequency of two expressions over time|

Figure 3: Monitoring the frequency of *Humanities Computing* vs.
*Digital Humanities*.

.. [#] Svensson, P. (2009). Humanities Computing as Digital Humanities.
       *Digital Humanities Quarterly 3(3)*. Available `here
       <http://digitalhumanities.org/dhq/vol/3/3/000065/000065.html>`_.


.. [#] The schema can be downloaded from :download:`here
       <schemas/humanist_for_textable_v2.0a3.ows>`. Note that two decades of
       Humanist archives weigh dozens of megabytes and that retrieving these
       data from the Internet can take a few minutes depending on bandwidth.
       Please be patient if Orange Textable appears to be stalled when the
       schema is being opened.