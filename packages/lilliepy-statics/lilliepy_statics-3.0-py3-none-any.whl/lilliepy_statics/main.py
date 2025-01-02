from reactpy import component, html
from pathlib import Path
import base64
import inspect

_pathway = None

def static(path_to_static_content):
    """
    Set the static directory path relative to the file that called this function.
    """
    global _pathway
    
    caller_frame = inspect.stack()[1]
    caller_file = Path(caller_frame.filename).resolve()
    
    caller_folder = caller_file.parent
    path = (caller_folder / path_to_static_content).resolve()
    
    if not path.exists():
        raise FileNotFoundError(f"Static content path {path} does not exist.")
    
    _pathway = path


@component
def use_CSS(css_file):
    """
    ReactPy component to load CSS content into a <style> tag.
    """
    global _pathway
    if _pathway is None:
        raise ValueError("Static path is not set. Call static() first.")
    
    css_path = _pathway / css_file
    if not css_path.exists():
        raise FileNotFoundError(f"CSS file {css_path} does not exist.")
    
    with open(css_path, 'r') as file:
        css_content = file.read()
    
    return html.style(css_content)

@component
def use_JS(js_file, module=False):
    """
    ReactPy component to load JS content into a <script> tag.
    """
    global _pathway
    if _pathway is None:
        raise ValueError("Static path is not set. Call static() first.")
    
    js_path = _pathway / js_file
    if not js_path.exists():
        raise FileNotFoundError(f"JS file {js_path} does not exist.")
    
    with open(js_path, 'r') as file:
        js_content = file.read()
    
    script_attrs = {"type": "module"} if module else {}
    
    return html.script(script_attrs, js_content)

@component
def use_Media(media_file, alt_text=""):
    """
    ReactPy component to handle image media files and embed them as Base64 data URIs.
    
    Parameters:
        media_file (str): The name of the media file (image only).
        alt_text (str): Alt text for the image file.
    """
    global _pathway
    if _pathway is None:
        raise ValueError("Static path is not set. Call static() first.")
    
    media_path = _pathway / media_file
    if not media_path.exists():
        raise FileNotFoundError(f"Media file {media_path} does not exist.")
    
    
    file_extension = media_path.suffix.lower()
    if file_extension in [".png"]:
        mime_type = "image/png"
    elif file_extension in [".jpg", ".jpeg"]:
        mime_type = "image/jpeg"
    elif file_extension in [".gif"]:
        mime_type = "image/gif"
    else:
        raise ValueError(f"Unsupported image file type: {file_extension}")
    
    
    with open(media_path, "rb") as file:
        image_data = file.read()
    base64_image = base64.b64encode(image_data).decode("utf-8")
    
    
    data_uri = f"data:{mime_type};base64,{base64_image}"
    
    
    return html.img({"src": data_uri, "alt": alt_text})