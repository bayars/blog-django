import React from 'react';
import { Box, Container, Typography, Button, Paper, useTheme, useMediaQuery } from '@mui/material';
import { motion } from 'framer-motion';
import DownloadIcon from '@mui/icons-material/Download';
import SchoolIcon from '@mui/icons-material/School';
import WorkIcon from '@mui/icons-material/Work';
import CodeIcon from '@mui/icons-material/Code';

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
        background: '#121212',
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
                fontSize: isMobile ? '2.5rem' : '4rem',
                color: 'white'
              }}
            >
              Resume
            </Typography>
          </MotionBox>
        </MotionBox>

        <Paper 
          elevation={3} 
          sx={{
            bgcolor: '#1E1E1E',
            borderRadius: 2,
            p: 4,
            mb: 4,
            border: '1px solid #333'
          }}
        >
          <MotionBox variants={itemVariants} sx={{ mb: 4 }}>
            <Box sx={{ display: 'flex', alignItems: 'center', gap: 2, mb: 2 }}>
              <SchoolIcon sx={{ color: '#64B5F6', fontSize: 32 }} />
              <Typography variant="h4" component="h2" sx={{ color: '#64B5F6', fontWeight: 600 }}>
                Education
              </Typography>
            </Box>
            <Typography variant="body1" sx={{ color: '#E0E0E0', lineHeight: 1.7 }}>
              Your education details here.
            </Typography>
          </MotionBox>

          <MotionBox variants={itemVariants} sx={{ mb: 4 }}>
            <Box sx={{ display: 'flex', alignItems: 'center', gap: 2, mb: 2 }}>
              <WorkIcon sx={{ color: '#64B5F6', fontSize: 32 }} />
              <Typography variant="h4" component="h2" sx={{ color: '#64B5F6', fontWeight: 600 }}>
                Experience
              </Typography>
            </Box>
            <Typography variant="body1" sx={{ color: '#E0E0E0', lineHeight: 1.7 }}>
              Your work experience details here.
            </Typography>
          </MotionBox>

          <MotionBox variants={itemVariants} sx={{ mb: 4 }}>
            <Box sx={{ display: 'flex', alignItems: 'center', gap: 2, mb: 2 }}>
              <CodeIcon sx={{ color: '#64B5F6', fontSize: 32 }} />
              <Typography variant="h4" component="h2" sx={{ color: '#64B5F6', fontWeight: 600 }}>
                Skills
              </Typography>
            </Box>
            <Typography variant="body1" sx={{ color: '#E0E0E0', lineHeight: 1.7 }}>
              Your skills details here.
            </Typography>
          </MotionBox>
        </Paper>

        <MotionBox variants={itemVariants} sx={{ textAlign: 'center' }}>
          <Button
            variant="contained"
            size="large"
            href="/static/resume.pdf"
            download
            startIcon={<DownloadIcon />}
            sx={{
              bgcolor: '#2C2C2C',
              color: '#64B5F6',
              border: '1px solid #444',
              px: 4,
              py: 1.5,
              borderRadius: 2,
              transition: 'all 0.3s ease',
              transform: 'scale(1)',
              '&:hover': {
                bgcolor: '#333',
                borderColor: '#64B5F6',
                transform: 'scale(1.05)',
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