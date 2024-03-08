from github import PullRequest

from get_predicted_popularity import get_predicted_popularity

LABELS = ['Criticality: zero', 'Criticality: low',
          'Criticality: mild', 'Criticality: high']


def get_label(popularity: float) -> str:
    if popularity < 100:
        return LABELS[0]
    elif popularity < 1000:
        return LABELS[1]
    elif popularity < 10000:
        return LABELS[2]
    else:
        return LABELS[3]


def label_translation(translation_pull_request: PullRequest):
    print(f"Labeling {translation_pull_request.title}")
    labels = translation_pull_request.get_labels()
    slug = translation_pull_request.title.split(": ")[1]
    popularity = get_predicted_popularity(slug)
    label_to_add = get_label(popularity)
    labels_to_remove = [label.name for label in labels if (label.name.startswith(
        "Criticality:") or label.name.startswith("Predicted:")) and label.name != label_to_add]
    if label_to_add not in labels:
        print(f"Adding {label_to_add} to {translation_pull_request.title}")
        translation_pull_request.add_to_labels(label_to_add)
    for label in labels_to_remove:
        print(f"Removing {label} from {translation_pull_request.title}")
        translation_pull_request.remove_from_labels(label)
