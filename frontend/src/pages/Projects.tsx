import React from 'react';
import { Box, Container, Typography, Grid, Card, CardContent, useTheme, useMediaQuery } from '@mui/material';
import { motion } from 'framer-motion';

const MotionBox = motion(Box);
const MotionCard = motion(Card);

const Projects: React.FC = () => {
  const theme = useTheme();
  const isMobile = useMediaQuery(theme.breakpoints.down('sm'));

  const projects = [
    { title: 'Project 1', description: 'Description for Project 1' },
    { title: 'Project 2', description: 'Description for Project 2' },
    { title: 'Project 3', description: 'Description for Project 3' },
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
              My Projects
            </Typography>
          </MotionBox>
        </MotionBox>

        <Grid container spacing={3} justifyContent="center">
          {projects.map((project, index) => (
            <Grid item xs={12} sm={6} md={4} key={project.title}>
              <MotionCard
                variants={itemVariants}
                whileHover={{ scale: 1.05 }}
                whileTap={{ scale: 0.95 }}
                sx={{
                  height: '100%',
                  background: 'rgba(255, 255, 255, 0.1)',
                  backdropFilter: 'blur(10px)',
                  border: '1px solid rgba(255, 255, 255, 0.2)',
                  '&:hover': {
                    background: 'rgba(255, 255, 255, 0.2)',
                  }
                }}
              >
                <CardContent sx={{ textAlign: 'center', py: 4 }}>
                  <Typography variant="h5" component="h2">
                    {project.title}
                  </Typography>
                  <Typography variant="body1" sx={{ mt: 2 }}>
                    {project.description}
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

export default Projects; 