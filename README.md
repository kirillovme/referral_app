# referral_app
 
## API Endpoints
### Request Authentication Code:

     URL: /auth/request/

Method: POST

Data Params: phone_number

Success Response: Code sent successfully

### Verify Authentication Code:

     URL: /auth/verify_code/

Method: POST

Data Params: code

Success Response: User profile data

### Get User Profile:

    URL: /profile/
Method: GET

Success Response: User profile data including referrals

### Activate Invite Code:

    URL: /activate_code//

Method: POST

Data Params: invite_code

Success Response: Updated user profile data

## Setup and Installation

docker-compose up -d


## Considerations

- Invite codes are unique across all users.
- Phone number verification is simulated with a 2-second delay.
- Users can only activate one invite code, and it must be a valid code from another user.