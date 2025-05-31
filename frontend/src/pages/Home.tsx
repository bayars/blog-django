import React from 'react';
import { 
  Box, 
  Container, 
  Typography, 
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
              Welcome to My Portfolio
            </Typography>
          </MotionBox>
          
          <MotionBox variants={itemVariants}>
            <Typography
              variant="h5"
              sx={{ mb: 4, opacity: 0.9, color: '#E0E0E0' }}
            >
              Software Engineer & Creative Developer
            </Typography>
          </MotionBox>
        </MotionBox>

        <Grid container spacing={3} justifyContent="center">
          {menuItems.map((item, index) => (
            <Grid item xs={12} sm={6} md={4} key={item.title}>
              <MotionCard
                variants={itemVariants}
                whileHover={{ scale: 1.05 }}
                whileTap={{ scale: 0.95 }}
                sx={{
                  height: '100%',
                  cursor: 'pointer',
                  bgcolor: '#1E1E1E',
                  border: '1px solid #333',
                  transition: 'all 0.3s ease',
                  '&:hover': {
                    bgcolor: '#252525',
                    borderColor: '#64B5F6',
                  }
                }}
                onClick={() => navigate(item.path)}
              >
                <CardContent sx={{ textAlign: 'center', py: 4 }}>
                  <Box sx={{ mb: 2 }}>
                    {React.cloneElement(item.icon, {
                      sx: { fontSize: 40, color: '#64B5F6' }
                    })}
                  </Box>
                  <Typography variant="h5" component="h2" sx={{ color: '#E0E0E0' }}>
                    {item.title}
                  </Typography>
                </CardContent>
              </MotionCard>
            </Grid>
          ))}
        </Grid>
      </Container>
    </Box>
  );
};

export default Home; 