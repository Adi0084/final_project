import logging

from demucs.apply import apply_model
from demucs.pretrained import get_model_from_args, ModelLoadingError


# TODO: Check again those issues
def separate(track_args: TrackArgs):
    try:
        model = get_model_from_args(track_args)
    except ModelLoadingError as error:
        logging.exception(error)

    model.cpu()
    model.eval()
    wav = load_track(track, 2, 44100)
    ref = wav.mean(0)
    wav = (wav - ref.mean()) / ref.std()
    sources = apply_model(model, wav[None], device='cuda', shifts=1,
                          split=True, overlap=0.25, progress=True,
                          num_workers=0)[0]
    sources = sources * ref.std() + ref.mean()
    channels_arr = []
    for source, name in zip(sources, model.sources):
        stem = out / track_args.filename.format(track=track.name.rsplit(".", 1)[0],
                                                trackext=track.name.rsplit(".", 1)[-1], stem=name, ext=ext)
        stem.parent.mkdir(parents=True, exist_ok=True)
        save_audio(source, str(stem), **kwargs)
        channels_arr.append(source)
    return channels_arr
