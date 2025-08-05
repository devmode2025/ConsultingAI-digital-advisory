# Static Images Directory

This directory contains static image assets for the ConsultingAI frontend.

## Image Assets

### Logo Files
- `logo.png` - ConsultingAI company logo (200x80px recommended)
- `consulting_bg.jpg` - Background image for consulting theme

### Diagrams
- `flow_diagram.png` - Society of Mind architecture flow diagram
- `som_architecture.png` - Complete SoM framework visualization

## Usage

Images are referenced in Streamlit components using relative paths:

```python
st.image("static/images/logo.png", width=200)
```

## Placeholder Images

For development, you can use text-based alternatives or generate placeholder images:

```python
# Text-based logo alternative
st.markdown("""
<div style="background: #1e3a8a; color: white; padding: 1rem; text-align: center;">
    🏢 ConsultingAI
</div>
""", unsafe_allow_html=True)
```

## Production Assets

Replace placeholder content with actual:
- Company branding assets
- Professional consulting imagery
- Custom architecture diagrams
- High-resolution icons and graphics