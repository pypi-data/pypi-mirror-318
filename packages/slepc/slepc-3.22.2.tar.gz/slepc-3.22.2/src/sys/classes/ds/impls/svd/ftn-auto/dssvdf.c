#include "petscsys.h"
#include "petscfix.h"
#include "petsc/private/fortranimpl.h"
/* dssvd.c */
/* Fortran interface file */

/*
* This file was generated automatically by bfort from the C source
* file.  
 */

#ifdef PETSC_USE_POINTER_CONVERSION
#if defined(__cplusplus)
extern "C" { 
#endif 
extern void *PetscToPointer(void*);
extern int PetscFromPointer(void *);
extern void PetscRmPointer(void*);
#if defined(__cplusplus)
} 
#endif 

#else

#define PetscToPointer(a) (a ? *(PetscFortranAddr *)(a) : 0)
#define PetscFromPointer(a) (PetscFortranAddr)(a)
#define PetscRmPointer(a)
#endif

#include "slepcds.h"
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define dssvdsetdimensions_ DSSVDSETDIMENSIONS
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define dssvdsetdimensions_ dssvdsetdimensions
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define dssvdgetdimensions_ DSSVDGETDIMENSIONS
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define dssvdgetdimensions_ dssvdgetdimensions
#endif
/* Provide declarations for malloc/free if needed for strings */
#include <stdlib.h>


/* Definitions of Fortran Wrapper routines */
#if defined(__cplusplus)
extern "C" {
#endif
SLEPC_EXTERN void  dssvdsetdimensions_(DS ds,PetscInt *m, int *ierr)
{
CHKFORTRANNULLOBJECT(ds);
*ierr = DSSVDSetDimensions(
	(DS)PetscToPointer((ds) ),*m);
}
SLEPC_EXTERN void  dssvdgetdimensions_(DS ds,PetscInt *m, int *ierr)
{
CHKFORTRANNULLOBJECT(ds);
CHKFORTRANNULLINTEGER(m);
*ierr = DSSVDGetDimensions(
	(DS)PetscToPointer((ds) ),m);
}
#if defined(__cplusplus)
}
#endif
