import pytest

import ilmsdump

from tests import data


@pytest.mark.asyncio
async def test_downlaod(client: ilmsdump.Client):
    attachments = [a async for a in data.HOMEWORK_201015.download(client)]

    assert (client.get_dir_for(data.HOMEWORK_201015) / 'index.html').exists()

    assert attachments == [
        data.ATTACHMENT_2038513,
        data.ATTACHMENT_2047732,
    ]


@pytest.mark.asyncio
async def test_download_invalid(client: ilmsdump.Client):
    invalid_homework = ilmsdump.Homework(
        id=0,
        title='invalid homework',
        course=data.COURSE_74,
    )

    with pytest.raises(ilmsdump.Unavailable):
        [a async for a in invalid_homework.download(client)]
