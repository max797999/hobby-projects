
Add-Type -AssemblyName Microsoft.VisualBasic

 

$term = [Microsoft.VisualBasic.Interaction]::InputBox("accountname", "Termed User AccountName")

 

$user = Get-ADUser $term -Properties Name

$username =  Get-ADuser $term -properties name | Select-Object name

$pphone = Get-ADUser -Identity $term -Properties ipPhone | Select-Object ipPhone


 

Get-ADPrincipalGroupMembership $term | Select-Object -ExpandProperty Name | Out-File -FilePath #Put in your file location

 

        # Remove user from all groups they are a member of

        Get-ADUser $term -Properties MemberOf | Select-Object -ExpandProperty MemberOf | ForEach-Object {

            Remove-ADGroupMember $_ -Member $term -Confirm:$false

        }

 

        # Set the user's employeeType attribute to Inactive and update Description

        Set-ADUser -Identity $term -Replace @{

            employeeType = 'Inactive'

            Description = "$date TERM"

            info = “$pphone”

        }

        set-aduser -Identity $term  -replace @{msexchhidefromaddresslists=$true}

 

        set-aduser -Identity $term -clear ipPhone

 

        # Set the user's password to never expire

        Set-ADUser -Identity $term -PasswordNeverExpires $True

 

        # Move the user to the _Termed_Monitoring OU

        Get-ADUser $term | Move-ADObject -TargetPath #Your AD target For users

       

        
      

        Write-Output "User $username has been processed successfully."