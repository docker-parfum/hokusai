from hokusai.lib.command import command
from hokusai.lib.common import print_green
from hokusai.services.deployment import Deployment
from hokusai.services.command_runner import CommandRunner
from hokusai.lib.exceptions import HokusaiError

@command
def promote(migration, constraint):
  deploy_from = Deployment('staging')
  tag = deploy_from.current_tag
  if tag is None:
    return -1
  print_green("Deploying tag %s to production..." % tag)

  if migration is not None:
    print_green("Running migration '%s' on production..." % migration)
    return_code = CommandRunner('production').run(tag, migration, constraint=constraint)
    if return_code:
      raise HokusaiError("Migration failed with return code %s" % return_code, return_code=return_code)


  deploy_to = Deployment('production').update(tag, constraint)
  print_green("Promoted staging to production at %s" % tag)
