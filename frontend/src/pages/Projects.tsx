import React from 'react';
import { Box, Container, Typography, Paper, Grid, Chip, IconButton, useTheme, useMediaQuery } from '@mui/material';
import { motion } from 'framer-motion';
import CodeIcon from '@mui/icons-material/Code';
import GitHubIcon from '@mui/icons-material/GitHub';
import LaunchIcon from '@mui/icons-material/Launch';

const MotionBox = motion(Box);

const Projects: React.FC = () => {
  const theme = useTheme();
  const isMobile = useMediaQuery(theme.breakpoints.down('sm'));

  const projects = [
    {
      title: 'Project 1',
      description: 'Description for Project 1',
      technologies: ['React', 'TypeScript', 'Node.js'],
      github: 'https://github.com/yourusername/project1',
      demo: 'https://project1-demo.com'
    },
    {
      title: 'Project 2',
      description: 'Description for Project 2',
      technologies: ['Python', 'Django', 'PostgreSQL'],
      github: 'https://github.com/yourusername/project2',
      demo: 'https://project2-demo.com'
    },
    {
      title: 'Project 3',
      description: 'Description for Project 3',
      technologies: ['React Native', 'Firebase', 'Redux'],
      github: 'https://github.com/yourusername/project3',
      demo: 'https://project3-demo.com'
    }
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
              My Projects
            </Typography>
          </MotionBox>
        </MotionBox>

        <Grid container spacing={3}>
          {projects.map((project) => (
            <Grid item xs={12} md={6} lg={4} key={project.title}>
              <MotionBox
                variants={itemVariants}
                whileHover={{ scale: 1.02 }}
                whileTap={{ scale: 0.98 }}
              >
                <Paper 
                  elevation={3}
                  sx={{
                    height: '100%',
                    bgcolor: '#1E1E1E',
                    borderRadius: 2,
                    p: 3,
                    border: '1px solid #333',
                    transition: 'all 0.3s ease',
                    '&:hover': {
                      bgcolor: '#252525',
                      borderColor: '#444'
                    }
                  }}
                >
                  <Box sx={{ display: 'flex', alignItems: 'center', gap: 2, mb: 2 }}>
                    <CodeIcon sx={{ color: '#64B5F6', fontSize: 32 }} />
                    <Typography variant="h5" component="h2" sx={{ color: '#64B5F6', fontWeight: 600 }}>
                      {project.title}
                    </Typography>
                  </Box>
                  
                  <Typography variant="body1" sx={{ color: '#E0E0E0', mb: 3 }}>
                    {project.description}
                  </Typography>

                  <Box sx={{ display: 'flex', flexWrap: 'wrap', gap: 1, mb: 3 }}>
                    {project.technologies.map((tech) => (
                      <Chip
                        key={tech}
                        label={tech}
                        size="small"
                        sx={{
                          bgcolor: '#2C2C2C',
                          color: '#64B5F6',
                          border: '1px solid #444',
                          '&:hover': {
                            bgcolor: '#333',
                          }
                        }}
                      />
                    ))}
                  </Box>

                  <Box sx={{ display: 'flex', gap: 2 }}>
                    <IconButton
                      href={project.github}
                      target="_blank"
                      rel="noopener noreferrer"
                      sx={{ 
                        color: '#888',
                        '&:hover': { 
                          color: '#64B5F6',
                          bgcolor: 'rgba(100, 181, 246, 0.1)'
                        }
                      }}
                    >
                      <GitHubIcon />
                    </IconButton>
                    <IconButton
                      href={project.demo}
                      target="_blank"
                      rel="noopener noreferrer"
                      sx={{ 
                        color: '#888',
                        '&:hover': { 
                          color: '#64B5F6',
                          bgcolor: 'rgba(100, 181, 246, 0.1)'
                        }
                      }}
                    >
                      <LaunchIcon />
                    </IconButton>
                  </Box>
                </Paper>
              </MotionBox>
            </Grid>
          ))}
        </Grid>
      </Container>
    </Box>
  );
};

export default Projects; 