# Docker Build Examples

## Personal Example

```bash
docker image build -t quay.somecompany.com/someuser/some-image -t quay.somecompany.com/someuser/some-image:$(cat docker/tag) --build-arg linux_username=some_linux_username --build-arg git_username="some git user" --build-arg git_user_email=someone@somecompany.com docker/.
```
