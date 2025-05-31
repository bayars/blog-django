import React from 'react';
import { Box, Container, Typography, Paper, useTheme, useMediaQuery } from '@mui/material';
import { motion } from 'framer-motion';
import PersonIcon from '@mui/icons-material/Person';
import EmailIcon from '@mui/icons-material/Email';
import LocationOnIcon from '@mui/icons-material/LocationOn';

const MotionBox = motion(Box);

const About: React.FC = () => {
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
              About Me
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
              <PersonIcon sx={{ color: '#64B5F6', fontSize: 32 }} />
              <Typography variant="h4" component="h2" sx={{ color: '#64B5F6', fontWeight: 600 }}>
                About Me
              </Typography>
            </Box>
            <Typography variant="body1" sx={{ color: '#E0E0E0', lineHeight: 1.7 }}>
              Your personal introduction here. Share your story, interests, and what drives you.
            </Typography>
          </MotionBox>

          <MotionBox variants={itemVariants} sx={{ mb: 4 }}>
            <Box sx={{ display: 'flex', alignItems: 'center', gap: 2, mb: 2 }}>
              <EmailIcon sx={{ color: '#64B5F6', fontSize: 32 }} />
              <Typography variant="h4" component="h2" sx={{ color: '#64B5F6', fontWeight: 600 }}>
                Contact
              </Typography>
            </Box>
            <Typography variant="body1" sx={{ color: '#E0E0E0', lineHeight: 1.7 }}>
              Your contact information here. Include your email, phone number, and any other relevant contact details.
            </Typography>
          </MotionBox>

          <MotionBox variants={itemVariants}>
            <Box sx={{ display: 'flex', alignItems: 'center', gap: 2, mb: 2 }}>
              <LocationOnIcon sx={{ color: '#64B5F6', fontSize: 32 }} />
              <Typography variant="h4" component="h2" sx={{ color: '#64B5F6', fontWeight: 600 }}>
                Location
              </Typography>
            </Box>
            <Typography variant="body1" sx={{ color: '#E0E0E0', lineHeight: 1.7 }}>
              Your location information here. Share where you're based and if you're open to remote work.
            </Typography>
          </MotionBox>
        </Paper>
      </Container>
    </Box>
  );
};

export default About; 