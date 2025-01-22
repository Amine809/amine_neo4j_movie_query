import React, { useState } from 'react';
import { Box, TextField, Button, Typography, Card, CardContent } from '@mui/material';
import axios from 'axios';

const QueryForm = () => {
  const [query, setQuery] = useState('');
  const [response, setResponse] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const res = await axios.post(
        'http://127.0.0.1:5000/query',
        { query },
        { headers: { 'Content-Type': 'application/json' } }
      );
      setResponse(res.data.response);
    } catch (error) {
      setResponse('Error occurred. Please try again.');
    }
  };

  return (
    <Box
      sx={{
        maxWidth: '800px',
        margin: '20px auto',
        padding: '20px',
        backgroundColor: 'white',
        boxShadow: 3,
        borderRadius: 2,
      }}
    >
      <Typography variant="h4" component="h1" gutterBottom>
        Enter Your Query
      </Typography>
      <form onSubmit={handleSubmit}>
        <TextField
          label="Query"
          variant="outlined"
          fullWidth
          multiline
          rows={4}
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          sx={{ marginBottom: '16px' }}
        />
        <Button variant="contained" color="primary" type="submit" fullWidth>
          Submit Query
        </Button>
      </form>

      {response && (
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
      )}
    </Box>
  );
};

export default QueryForm;
