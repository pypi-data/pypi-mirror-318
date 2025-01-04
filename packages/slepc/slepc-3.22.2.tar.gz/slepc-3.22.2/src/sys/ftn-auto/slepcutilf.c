#include "petscsys.h"
#include "petscfix.h"
#include "petsc/private/fortranimpl.h"
/* slepcutil.c */
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

#include "slepcsys.h"
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define slepchasexternalpackage_ SLEPCHASEXTERNALPACKAGE
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define slepchasexternalpackage_ slepchasexternalpackage
#endif
/* Provide declarations for malloc/free if needed for strings */
#include <stdlib.h>


/* Definitions of Fortran Wrapper routines */
#if defined(__cplusplus)
extern "C" {
#endif
SLEPC_EXTERN void  slepchasexternalpackage_( char pkg[],PetscBool *has, int *ierr, PETSC_FORTRAN_CHARLEN_T cl0)
{
  char *_cltmp0 = PETSC_NULLPTR;
/* insert Fortran-to-C conversion for pkg */
  FIXCHAR(pkg,cl0,_cltmp0);
*ierr = SlepcHasExternalPackage(_cltmp0,has);
  FREECHAR(pkg,_cltmp0);
}
#if defined(__cplusplus)
}
#endif
