---
id: C06-006
title: RAG Beyond Texts
source_pages: "530-534"
chapter: 6
concepts: [multimodal-rag, clip-embeddings, tabular-rag, text-to-sql, sql-execution, semantic-parsing, tool-use]
related: [C06-005, C06-007, C06-008]
time_sensitive: false
---
# RAG Beyond Texts
(Source: PDF pp. 530-534; the closing paragraph of the RAG part on PDF p. 535, above the "Agents" heading, is also part of this section. The box "Evaluating Retrieval Solutions" at the top of PDF p. 530 belongs to C06-005.)

## What the section covers
Text-based RAG uses text documents as external sources. This section extends RAG to two other kinds of external data: multimodal data (images, video, audio) and tabular data (PDF pp. 530-531).

## Multimodal RAG
- If the generator is multimodal, its context can be augmented with images, videos, audio and so on from external sources, not only text. The book uses images as its running example and says any modality can be substituted (PDF p. 531).
- Given a query, the retriever fetches both texts and images. Example: for "What's the color of the house in the Pixar movie Up?", the retriever can fetch a picture of the house to help the model answer (Figure 6-6; the real image is not shown for copyright reasons) (PDF p. 531). The figure shows a text database and an image database both feeding a retriever; the user query "What's the color of the house in Up?" goes to the retriever and also directly to the generative model; the retriever passes on a retrieved text snippet ("Inside, the house from Up ...") and an image of the house (a drawn stand-in with balloons), and the generative model returns the response to the user (PDF p. 531).
- Retrieval via metadata: if images carry titles, tags or captions, they can be retrieved on that metadata, for instance when a caption is judged relevant to the query (PDF p. 532).
- Retrieval via content: you need a way to compare images with queries. For text queries this takes a multimodal embedding model that embeds both images and text. Using CLIP (Radford et al., 2021) as the example, the retriever works in three steps (PDF p. 532):
  1. Generate CLIP embeddings for all data, texts and images, and store them in a vector database.
  2. Generate the CLIP embedding of the query.
  3. Query the vector database for all images and texts whose embeddings are close to the query embedding.

## RAG with tabular data
- Most applications deal with tabular data as well as unstructured text and images, and many queries need facts from tables. The workflow for augmenting context with tables differs significantly from the classic RAG workflow (PDF p. 532).
- Running example: Kitty Vogue, an imaginary ecommerce site specializing in cat fashion, with an order table named Sales (Table 6-3). Visible columns are Order ID, Timestamp, Product ID, Product and a unit/price column; sample rows: order 1, product 2044 Meow Mix Seasoning, 10.99; order 2, product 3492 Purr & Shake, 25; order 3, product 2045 Fruity Fedora, 18; timestamps are shown as ellipses (PDF pp. 532-533). The table is clipped at the right edge in the PDF, so further columns are cut off. UNVERIFIED: the full header of the clipped column (it reads "Unit" and the first value reads 10.99 with the last digit partly cut) and any columns beyond it in Table 6-3. Figure 6-7 on PDF p. 534 shows the same table with columns Timestamp, Product ID, Product name, Price/unit ($), Units and Total (rows: 2044 Meow Mix Seasoning 10.99, 1 unit, total 10.99; 3492 Purr & Shake 25, 2 units, total 50; 2045 Fruity Fedora 18, 1 unit, total 18) (PDF p. 534).
- Question: "How many units of Fruity Fedora were sold in the last 7 days?" The system must query the table for all orders involving Fruity Fedora and sum the units. If the table supports SQL, the query selects SUM(units) as total_units_sold from Sales where product_name is 'Fruity Fedora' and timestamp is at or after the current date minus 7 days (the printed query is cut off at the right edge in the PDF, ending around "INTERVAL 7 D", so the final unit keyword is not visible) (PDF p. 533).
- The workflow needs a system that can generate and execute SQL (Figure 6-7) (PDF pp. 533-534):
  1. Text-to-SQL: from the user query and the table schemas, decide which SQL query is needed. This is an example of semantic parsing, discussed in Chapter 2.
  2. SQL execution: run the query.
  3. Generation: produce a response from the SQL result and the original user query.
  The figure shows the user query and the table going into the text-to-SQL and SQL-execution stages, the SQL result going to the generative model together with the original query, and the response returned to the user (PDF p. 534).
- When there are many tables whose schemas cannot all fit in the model's context, add an intermediate step that predicts which tables each query needs. Text-to-SQL can be done by the same generator that writes the final response or by a specialized text-to-SQL model (PDF p. 534).

## Bridge to agents
Retrievers and SQL executors are tools that let a model handle more queries and respond better. The book asks whether giving a model more tools would improve it further, noting that tool use is a core characteristic of the agentic pattern, the topic of the next section (PDF p. 535).

## Relations
Extends the text RAG material in C06-005 and the earlier RAG sections. The tabular RAG system is later reused as a simple agent in C06-008, and the agent section begins in C06-007.
