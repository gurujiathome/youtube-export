from util import popen_results

def upload_unconverted(video_filename, video_path):

    s3_url = "s3://KA-youtube-unconverted/%s" % video_filename

    command_args = ["s3cmd/s3cmd", "put", video_path, s3_url]
    results = popen_results(command_args)
    print results

    return s3_url