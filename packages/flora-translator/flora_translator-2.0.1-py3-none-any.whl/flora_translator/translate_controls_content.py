from .translate_using_google import translate_using_google
import flet, threading, asyncio

allowed_props_to_translate = ["value", "label", "tooltip", "text", "semantics_label"]

def translate_control_content (TranslateFletPage_class, control:flet.Control, use_internet:bool=True, update_async=False):
    """
    This function translate the control content.

    It create an attr (last_translated_texts:dict) in the control that stores the last translated
    texts so it reduces unnecessary translation requests.
    """

    if type(control) is flet.TextField or hasattr(control,"data") and control.data == "no_translate":
        allowed_props_to_translate_local = ["label", "tooltip", "semantics_label"]
    else:
        allowed_props_to_translate_local = allowed_props_to_translate

    # Check if the control is skiped so not translate it.
    if control in TranslateFletPage_class.skiped_controls: return
    if control == None: return

    # start translating the control
    for p in allowed_props_to_translate_local:
        if hasattr(control, str(p)):
            value = getattr(control, str(p))
            if use_internet and value != None and type(value) == str:
                r = translate_using_google(
                    src=value,
                    from_language=TranslateFletPage_class.from_language.value,
                    into_language=TranslateFletPage_class.into_language.value
                )
                setattr(control, str(p), str(r))

    sub_controls_names = ["controls", "tabs", "actions","spans"]
    for i in sub_controls_names:
        if hasattr(control, i):
            for i in getattr(control, str(i)):
                threading.Thread(target=translate_control_content, kwargs={
                    "TranslateFletPage_class" : TranslateFletPage_class,
                    "control" : i,
                    "use_internet" : use_internet
                }, daemon=True).start()
                # translate_control_content(TranslateFletPage_class, i, use_internet)

    sub_contents_names = ["content", "leading", "title"]
    for ic in sub_contents_names:
        if hasattr(control, ic):
            threading.Thread(target=translate_control_content, kwargs={
                        "TranslateFletPage_class" : TranslateFletPage_class,
                        "control" : getattr(control, ic),
                        "use_internet" : use_internet
                    }, daemon=True).start()

    try:
        if control.page != None:
            if update_async:
                asyncio.create_task(control.update_async())
            else:
                control.update()
    except:
        pass
