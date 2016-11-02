#!/usr/bin/python

import requests


class Client(object):
    def __init__(self, token, domain, debug=False):
        assert isinstance(token, str)
        assert isinstance(domain, str)

        self.token = token
        self.domain = domain
        self.debug = debug

    def _do_query(self, resource):
        base = 'http://{domain}/api/0'.format(token=self.token, domain=self.domain)
        url = base + resource

        if self.debug:
            print (url)

        return requests.get(url, auth=requests.auth.HTTPBasicAuth(self.token, '')).json()

    def get_organizations(self):
        return self._do_query('/organizations/')

    def get_organization(self, organization_slug):
        return self._do_query('/organizations/{o}/'.format(o=organization_slug))

    def get_projects(self, organization_slug):
        return self._do_query('/{o}/projects/'.format(o=organization_slug))

    def get_project(self, project, organization_slug):
        return self._do_query('/projects/{o}/{p}/'.format(o=organization_slug, p=project))

    def get_groups(self, project, organization_slug):
        return self._do_query('/projects/{o}/{p}/groups/'.format(o=organization_slug, p=project))

    def get_group(self, group_id):
        return self._do_query('/groups/{g}/'.format(g=str(group_id)))

    def get_events(self, group_id):
        return self._do_query('/groups/{g}/events/'.format(g=str(group_id)))

    def get_event(self, event_id):
        return self._do_query('/events/{e}/'.format(e=str(event_id)))

