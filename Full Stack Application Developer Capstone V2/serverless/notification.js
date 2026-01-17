// serverless/notification.js (IBM Cloud Function)
function main(params) {
    const { patientId, condition, confidence } = params;
    
    // Send notification to healthcare provider
    const message = `High-risk assessment detected for patient ${patientId}: ${condition} (${confidence}% confidence)`;
    
    // In real implementation: Send SMS/email via Twilio/SendGrid
    console.log(message);
    
    return {
        statusCode: 200,
        body: { notification: 'sent' }
    };
}