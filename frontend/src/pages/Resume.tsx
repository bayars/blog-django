import React from 'react';
import { Box, Container, Typography, Button, useTheme, useMediaQuery } from '@mui/material';
import { motion } from 'framer-motion';

const MotionBox = motion(Box);

const Resume: React.FC = () => {
  const theme = useTheme();
  const isMobile = useMediaQuery(theme.breakpoints.down('sm'));

  const containerVariants = {
    hidden: { opacity: 0 },
    visible: {
      opacity: 1,
      transition: {
        staggerChildren: 0.1
      }
    }
  };

  const itemVariants = {
    hidden: { y: 20, opacity: 0 },
    visible: {
      y: 0,
      opacity: 1,
      transition: {
        duration: 0.5
      }
    }
  };

  return (
    <Box
      sx={{
        minHeight: '100vh',
        background: 'linear-gradient(45deg, #1a237e 30%, #0d47a1 90%)',
        color: 'white',
        py: 8
      }}
    >
      <Container maxWidth="lg">
        <MotionBox
          initial="hidden"
          animate="visible"
          variants={containerVariants}
          sx={{ textAlign: 'center', mb: 8 }}
        >
          <MotionBox variants={itemVariants}>
            <Typography
              variant="h2"
              component="h1"
              sx={{
                fontWeight: 'bold',
                mb: 2,
                fontSize: isMobile ? '2.5rem' : '4rem'
              }}
            >
              My Resume
            </Typography>
          </MotionBox>
        </MotionBox>

        <MotionBox variants={itemVariants} sx={{ mb: 4 }}>
          <Typography variant="h4" component="h2" sx={{ mb: 2 }}>
            Education
          </Typography>
          <Typography variant="body1" sx={{ mb: 2 }}>
            Your education details here.
          </Typography>
        </MotionBox>

        <MotionBox variants={itemVariants} sx={{ mb: 4 }}>
          <Typography variant="h4" component="h2" sx={{ mb: 2 }}>
            Experience
          </Typography>
          <Typography variant="body1" sx={{ mb: 2 }}>
            Your work experience details here.
          </Typography>
        </MotionBox>

        <MotionBox variants={itemVariants} sx={{ mb: 4 }}>
          <Typography variant="h4" component="h2" sx={{ mb: 2 }}>
            Skills
          </Typography>
          <Typography variant="body1" sx={{ mb: 2 }}>
            Your skills details here.
          </Typography>
        </MotionBox>

        <MotionBox variants={itemVariants} sx={{ textAlign: 'center', mt: 6 }}>
          <Button
            variant="contained"
            size="large"
            href="/static/resume.pdf"
            download
            sx={{
              background: 'rgba(255, 255, 255, 0.2)',
              backdropFilter: 'blur(10px)',
              '&:hover': {
                background: 'rgba(255, 255, 255, 0.3)',
              }
            }}
          >
            Download Resume
          </Button>
        </MotionBox>
      </Container>
    </Box>
  );
};

export default Resume; 