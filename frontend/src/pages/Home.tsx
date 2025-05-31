import React from 'react';
import { 
  Box, 
  Container, 
  Typography, 
  Button, 
  Grid, 
  Card, 
  CardContent,
  useTheme,
  useMediaQuery
} from '@mui/material';
import { motion } from 'framer-motion';
import { 
  Code as CodeIcon,
  Work as WorkIcon,
  PhotoLibrary as GalleryIcon,
  Article as BlogIcon,
  Person as AboutIcon
} from '@mui/icons-material';
import { useNavigate } from 'react-router-dom';

const MotionBox = motion(Box);
const MotionCard = motion(Card);

const Home: React.FC = () => {
  const theme = useTheme();
  const isMobile = useMediaQuery(theme.breakpoints.down('sm'));
  const navigate = useNavigate();

  const menuItems = [
    { title: 'Projects', icon: <CodeIcon />, path: '/projects' },
    { title: 'Resume', icon: <WorkIcon />, path: '/resume' },
    { title: 'Gallery', icon: <GalleryIcon />, path: '/gallery' },
    { title: 'Blog', icon: <BlogIcon />, path: '/blog' },
    { title: 'About', icon: <AboutIcon />, path: '/about' },
  ];

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
              Welcome to My Portfolio
            </Typography>
          </MotionBox>
          
          <MotionBox variants={itemVariants}>
            <Typography
              variant="h5"
              sx={{ mb: 4, opacity: 0.9 }}
            >
              Software Engineer & Creative Developer
            </Typography>
          </MotionBox>
        </MotionBox>

        <Grid container spacing={3} justifyContent="center">
          {menuItems.map((item, index) => (
            <Grid component="div" item xs={12} sm={6} md={4} key={item.title}>
              <MotionCard
                variants={itemVariants}
                whileHover={{ scale: 1.05 }}
                whileTap={{ scale: 0.95 }}
                sx={{
                  height: '100%',
                  cursor: 'pointer',
                  background: 'rgba(255, 255, 255, 0.1)',
                  backdropFilter: 'blur(10px)',
                  border: '1px solid rgba(255, 255, 255, 0.2)',
                  '&:hover': {
                    background: 'rgba(255, 255, 255, 0.2)',
                  }
                }}
                onClick={() => navigate(item.path)}
              >
                <CardContent sx={{ textAlign: 'center', py: 4 }}>
                  <Box sx={{ mb: 2 }}>
                    {React.cloneElement(item.icon, {
                      sx: { fontSize: 40, color: 'white' }
                    })}
                  </Box>
                  <Typography variant="h5" component="h2">
                    {item.title}
                  </Typography>
                </CardContent>
              </MotionCard>
            </Grid>
          ))}
        </Grid>

        <MotionBox
          variants={itemVariants}
          sx={{ textAlign: 'center', mt: 6 }}
        >
          <Button
            variant="contained"
            size="large"
            onClick={() => window.open('mailto:your.email@example.com')}
            sx={{
              background: 'rgba(255, 255, 255, 0.2)',
              backdropFilter: 'blur(10px)',
              '&:hover': {
                background: 'rgba(255, 255, 255, 0.3)',
              }
            }}
          >
            Contact Me
          </Button>
        </MotionBox>
      </Container>
    </Box>
  );
};

export default Home; 