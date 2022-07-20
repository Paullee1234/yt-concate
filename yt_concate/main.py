from yt_concate.pipeline.steps.get_vedio_list import GetVideoList
from yt_concate.pipeline.steps.step import StepException
from yt_concate.pipeline.pipeline import Pipeline

CHANNEL_ID = 'UC-XWpctw55Q6b_AHo8rkJgw'


def main():
    inputs = {
        'channel_id': CHANNEL_ID,
    }
    steps = [
        GetVideoList(),
    ]

    p = Pipeline(steps)
    p.run(inputs)


if __name__ == '__main__':
    main()

