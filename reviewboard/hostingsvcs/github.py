from django.utils import simplejson
                                 '%(github_public_repo_name)s/issues#issue/%%s',
    supports_bug_trackers = True
                body=simplejson.dumps(body))
                rsp = simplejson.loads(data)
                                           body=simplejson.dumps(post_data))
                rsp = simplejson.loads(e.read())