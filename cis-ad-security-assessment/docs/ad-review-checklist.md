# Active Directory Review Checklist

## Structure
- [ ] Forest and domain design justified (single forest/domain where possible)
- [ ] OU structure supports delegation and Group Policy targeting
- [ ] RODCs used in low-trust locations
- [ ] Entra ID connect scope and sync account reviewed

## Privileged access
- [ ] Domain/Enterprise/Schema Admin membership minimal and reviewed
- [ ] Separate admin accounts; no daily-use accounts in privileged groups
- [ ] Admin tiering (Tier 0/1/2) defined
- [ ] Service accounts inventoried; managed service accounts where possible

## Hygiene
- [ ] Stale users and computers removed or disabled
- [ ] Password policy and fine-grained policies reviewed
- [ ] Kerberoastable accounts and delegation settings reviewed
- [ ] SMB signing and LDAP signing enforced
- [ ] Legacy protocols (NTLMv1, SMBv1) disabled
- [ ] Backups of AD tested; recovery documented
