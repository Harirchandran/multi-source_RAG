# app/streamlit_app.py
import sys
import os
import tempfile

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
from main import run_query, check_index_exists, add_source_to_index, get_sources, delete_index

st.title("RAG QA System")

# Sidebar for Source Management
with st.sidebar:
    st.header("Database Management")
    
    # Check index availability
    if check_index_exists():
        st.success("✅ Index Available")
        
        sources = get_sources()
        if sources:
            with st.expander("View Indexed Sources"):
                for s in sources:
                    st.write(f"- **{s['name']}** ({s['type']})")
                    
        if st.button("🗑️ Delete Entire Database", type="primary"):
            delete_index()
            st.rerun()
    else:
        st.warning("⚠️ No database found. Add a source to begin.")

    st.divider()
    st.subheader("Add New Source")
    source_type = st.selectbox("Source Type", ["Web Link", "PDF File", "Text File"])
    
    if source_type == "Web Link":
        url = st.text_input("Enter URL:")
        if st.button("Process URL"):
            if url.startswith("http"):
                with st.spinner("Scraping and indexing URL..."):
                    add_source_to_index(url, "web", source_name=url)
                st.success("Successfully added to index!")
                st.rerun()
            else:
                st.error("Please enter a valid URL.")
                
    elif source_type in ["PDF File", "Text File"]:
        uploaded_file = st.file_uploader(f"Upload your {source_type}", type=["pdf"] if source_type == "PDF File" else ["txt"])
        
        if st.button(f"Process {source_type}") and uploaded_file is not None:
            with st.spinner("Processing file..."):
                suffix = ".pdf" if source_type == "PDF File" else ".txt"
                stype = "pdf" if source_type == "PDF File" else "text"
                
                with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp_file:
                    tmp_file.write(uploaded_file.getvalue())
                    tmp_path = tmp_file.name
                
                try:
                    add_source_to_index(tmp_path, stype, source_name=uploaded_file.name)
                    st.success("Successfully added to index!")
                except Exception as e:
                    st.error(str(e))
                    st.stop()
                finally:
                    os.unlink(tmp_path)
                st.rerun()

# Main Chat Area
query = st.text_input("Ask a question")

if query:
    if not check_index_exists():
        st.error("Please add a source from the sidebar before asking a question!")
    else:
        with st.spinner("Thinking..."):
            answer, docs = run_query(query)

        st.subheader("Answer")
        st.write(answer)

        with st.expander("Sources"):
            for i, doc in enumerate(docs):
                st.write(f"**Source {i+1}:**")
                st.write(doc.page_content[:300])
                st.write("---")