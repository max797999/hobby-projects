Add-Type -AssemblyName Microsoft.VisualBasic

Connect-ExchangeOnline
connect-azureAD

$term = [Microsoft.VisualBasic.Interaction]::InputBox("accountemail", "Termed User email address")

$transition = [Microsoft.VisualBasic.Interaction]::InputBox("email address","Transitioning User email address")

 

$user = get-azureADuser -ObjectId $term | select -ExpandProperty displayname

$Transitionuser = get-azureADuser  -ObjectId $transition | select -ExpandProperty displayname

$phoneNumber = get-azureADuser -ObjectId $transition | select -ExpandProperty  telephoneNumber

$Transitionuser= get-azureADuser -ObjectId $transition |  select -ExpandProperty mail

 

$OOO = "$user is no longer with The business. For assistance, please contact $Transitionuser at $phoneNumber or via email at $Transitionuser. Thank you."

Set-MailboxAutoReplyConfiguration -Identity $term -AutoReplyState enabled -internalmessage $OOO -externalmessage $OOO  -ExternalAudience all

Add-MailboxPermission -Identity $term -User $transition -AccessRights FullAccess

Set-Mailbox -Identity $term -type shared

Disconnect-ExchangeOnline -Confirm:$false
Disconnect-AzureAD -Confirm:$false