import React from 'react';
import { Card, CardContent, Typography } from '@mui/material';

const ResponseCard = ({ response }) => {
  return (
    <Card sx={{ marginTop: '20px', backgroundColor: '#f1f1f1' }}>
      <CardContent>
        <Typography variant="h6" component="h2">
          Response:
        </Typography>
        <pre style={{ whiteSpace: 'pre-wrap' }}>
          {JSON.stringify(response, null, 2)}
        </pre>
      </CardContent>
    </Card>
  );
};

export default ResponseCard;
